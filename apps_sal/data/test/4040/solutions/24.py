n, m, d = list(map(int, input().split()))

lengths = list(map(int, input().split()))
poses = [n + 1] * (m + 1)
index = m - 1
while index >= 0:
    poses[index] = poses[index + 1] - lengths[index]
    index -= 1

# print(poses)

cur = 0
ind = 0
result = True
while cur < n + 1:
    if cur + d >= n + 1:
        break
    if ind == m:
        result = False
        break
    if cur + d <= poses[ind]:
        poses[ind] = cur + d
        cur = cur + d + lengths[ind] - 1
        ind += 1
    else:
        break

if result:
    print("YES")
    poses.append(0)
    lengths.append(0)
    lengths.append(1)
    res = []
    for ind, it in enumerate(poses[:-1]):
        for _ in range(it - poses[ind - 1] - lengths[ind - 1]):
            res.append('0')
        for _ in range(lengths[ind]):
            res.append(str(ind + 1))
    print(" ".join(res))
else:
    print("NO")
