from sys import stdin
def nii(): return map(int, stdin.readline().split())
def lnii(): return list(map(int, stdin.readline().split()))


a, b = nii()

num = 1
ans = 0
while num < b:
    ans += 1
    num += a - 1

print(ans)
