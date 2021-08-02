N = int(input())
a = list(map(int, input().split()))

pos_L = -1
for i in range(1, len(a)):
    if a[i] < a[i - 1]:
        pos_L = i - 1
        break

if pos_L == -1:
    print('yes')
    print('1 1')
    return

pos_R = -1;
for i in range(len(a) - 1, 0, -1):
    if a[i] < a[i - 1]:
        pos_R = i
        break

if pos_R == -1:
    print('yes')
    print(1, N)
    return

half_len = (pos_R - pos_L + 1) // 2
for i in range(pos_L, pos_L + half_len):
    a[i], a[pos_R + pos_L - i] = a[pos_R + pos_L - i], a[i];

for i in range(1, len(a)):
    if a[i] < a[i - 1]:
        print('no')
        return

print('yes')
print(pos_L + 1, pos_R + 1)
