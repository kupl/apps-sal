n, m = list(map(int, input().split()))
s = list(input())[::-1]
i = 0
ans = 0
ans_list = []
while i < n:
    l = s[i+1:i+m+1]
    for next in range(m-1, -2, -1):
        if next == -1:
            print((-1))
            return
        if next > len(l)-1:
            continue
        if l[next] == '0':
            ans_list.append(next+1)
            i += next+1
            break
print((' '.join(map(str, ans_list[::-1]))))

