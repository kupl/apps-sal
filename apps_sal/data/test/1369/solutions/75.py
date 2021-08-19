import numpy as np
EPS = 1e-12


class MinEnclosingCircle:

    def __init__(self, pts):
        self.pts = pts
        self.center = None
        self.radius = None

    def fit(self):
        self.center = (self.pts[0] + self.pts[1]) / 2
        self.radius = np.linalg.norm(self.pts[0] - self.pts[1]) / 2 + EPS
        for i in range(2, len(self.pts)):
            distance = np.linalg.norm(self.pts[i] - self.center)
            if distance >= self.radius:
                (self.center, self.radius) = self.find_second_point(i)

    def find_second_point(self, i):
        center = (self.pts[0] + self.pts[i]) / 2
        radius = np.linalg.norm(self.pts[0] - self.pts[i]) / 2 + EPS
        for j in range(1, i):
            distance = np.linalg.norm(self.pts[j] - center)
            if distance >= radius:
                (new_center, new_radius) = self.find_third_point(i, j)
                if new_radius > 0:
                    center = new_center
                    radius = new_radius
        return (center, radius)

    def find_third_point(self, i, j):
        center = (self.pts[j] + self.pts[i]) / 2
        radius = np.linalg.norm(self.pts[j] - self.pts[i]) / 2 + EPS
        for k in range(j):
            distance = np.linalg.norm(self.pts[k] - center)
            if distance >= radius:
                (new_center, new_radius) = self.find_circle_3pts(i, j, k)
                if new_radius > 0:
                    center = new_center
                    radius = new_radius
        return (center, radius)

    def find_circle_3pts(self, i, j, k):
        v1 = self.pts[j] - self.pts[i]
        v2 = self.pts[k] - self.pts[i]
        mid_point1 = (self.pts[j] + self.pts[i]) / 2
        c1 = np.dot(mid_point1, v1)
        mid_point2 = (self.pts[k] + self.pts[i]) / 2
        c2 = np.dot(mid_point2, v2)
        det = np.cross(v1, v2)
        if abs(det) <= EPS:
            d1 = np.sum(v1 * v1)
            d2 = np.sum(v2 * v2)
            d3 = np.sum((v1 - v2) ** 2)
            radius = np.sqrt(max(d1, d2, d3)) / 2 + EPS
            if d1 >= d2 and d1 >= d3:
                center = (self.pts[i] + self.pts[j]) / 2
            elif d2 >= d1 and d2 >= d3:
                center = (self.pts[i] + self.pts[k]) / 2
            else:
                center = (self.pts[j] + self.pts[k]) / 2
        else:
            center = np.zeros_like(v1)
            center[0] = c1 * v2[1] - c2 * v1[1]
            center[1] = v1[0] * c2 - v2[0] * c1
            center = center / det
            radius = np.linalg.norm(center - self.pts[i]) + EPS
        return (center, radius)


n = int(input())
point = [np.array(input().split(), dtype=int) for _ in range(n)]
mec = MinEnclosingCircle(point)
mec.fit()
print(mec.radius)
