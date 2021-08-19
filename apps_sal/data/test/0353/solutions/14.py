from sys import stdin as fin
# fin = open("cfr373a.in")

n = int(fin.readline())
# n, m = map(int, fin.readline.split())
nums = tuple(map(int, fin.readline().split()))

ans = {15: "DOWN", 0: "UP"}
if nums[-1] in ans:
    print(ans[nums[-1]])
elif len(nums) == 1:
    print(-1)
else:
    print("DOWN" if nums[-1] < nums[-2] else "UP")
