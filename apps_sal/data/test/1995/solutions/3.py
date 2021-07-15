word = input()
N = int(input())

query = []
for i in range(N):
    q = input().split()
    query.append(list(map(int, q)))

for q in query:
    l, r, k = q[0] - 1, q[1] - 1, q[2]
    k = k % (r - l + 1)
    if l == r or k == 0:
        continue
    word = word[0:l] + word[r-k+1:r+1] + word[l:r-k+1] + word[r+1:]

print(word)
