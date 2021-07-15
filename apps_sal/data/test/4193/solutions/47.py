import numpy as np

arr = np.array([list(map(int, input().split())) for _ in range(3)])


n = int(input())

for _ in range(n):
    b = int(input())
    arr[np.where(arr == b)] = 0

ans1 = (np.sum(arr, axis=0) == 0).sum() >= 1
ans2 = (np.sum(arr, axis=1) == 0).sum() >= 1
ans3 = (np.diag(arr) == 0).sum() == 3
ans4 = (np.diag(np.rot90(arr)) == 0).sum() == 3

print("Yes" if ans1 or ans2 or ans3 or ans4 else "No")
