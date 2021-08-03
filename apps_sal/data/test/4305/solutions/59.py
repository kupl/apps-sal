[H, A] = [int(i) for i in input().split()]
t = 0
if H / A != int(H / A):
    t = 1
print(int(H / A) + t)
