arr = list(input())
done = [False] * len(arr)

tar = list('abcdefghijklmnopqrstuvwxyz')
ti = 0

obs = True

for i in range(len(arr)):
    if done[i]:
        continue

    if tar[ti] != arr[i]:
        obs = False
        break

    ti += 1
    for j in range(i + 1, len(arr)):
        if done[j]:
            continue
        if arr[j] == arr[i]:
            done[j] = True

if obs:
    print('YES')
else:
    print('NO')
