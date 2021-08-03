class Solution:
    def racecar(self, target: int) -> int:
        front = [(0, 1)]
        visited = {(0, 1): 0}
        while front != []:
            nf = []
            for (pos, speed) in front:
                aa = [(pos + speed, speed * 2), (pos, -1)] if speed > 0 else [(pos + speed, speed * 2), (pos, 1)]
                for v in aa:
                    if not v in visited:
                        visited[v] = visited[(pos, speed)] + 1
                        nf.append(v)
                        if v[0] == target:
                            return visited[v]
            front = nf
