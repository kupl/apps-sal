# zadacha B
a, b = list(map(int, input().split()))
k1, k2 = list(map(int, input().split()))
k3, k4 = list(map(int, input().split()))

if (k1 + k3 <= a and (k2 <= b and k4 <= b)) or (k1 + k3 <= b and (k2 <= a and k4 <= a)) or (
                    k1 + k4 <= a and (k2 <= b and k4 <= b)) or (k1 + k4 <= b and (k2 <= a and k4 <= a)) or (
                    k2 + k4 <= a and (k1 <= b and k3 <= b)) or (
                    k2 + k4 <= b and (k1 <= a and k3 <= a)) or (k1 + k4 <= a and (k2 <= b and k3 <= b)) or (
            k1 + k4 <= b and (k2 <= a and k3 <= a)) or (k2 + k3 <= a and (k1 <= b and k4 <= b)) or (
            k2 + k3 <= b and (k1 <= a and k4 <= a)):
    print("YES")
else:
    print("NO")

