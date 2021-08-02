
N = int(input())
H = list(map(int, input().split()))

h_list = [H[0]]
cnt = 1
for i in range(1, N):
    h_list.append(H[i])

    if max(h_list) == H[i]:
        cnt += 1
print(cnt)
