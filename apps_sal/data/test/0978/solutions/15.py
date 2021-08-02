a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
k = int(input())
for i in range(0, 4):
    b = input()
    for j in range(0, 4):
        if b[j] != '.':
            a[int(b[j])] += 1
for i in range(0, 10):
    if a[i] > k * 2:
        print("NO")
        return
print("YES")
