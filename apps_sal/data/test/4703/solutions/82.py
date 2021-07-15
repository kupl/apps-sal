
n = str(input())

len_n = len(n)-1

ans = 0
total = 0

for i in range(2**len_n):
    temp = n[0]
    for j in range(len_n):
        if (i >> j) & 1:
            temp += '+'
        temp += n[j+1]
    total = list(map(int, temp.split('+')))
    ans += sum(total)

print(ans)
