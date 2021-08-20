n = int(input())
sl = list(map(int, input().split()))
ans = ''
current = 0
for i in range(n):
    if current < sl[0] and current < sl[-1]:
        if sl[0] == sl[-1] and i != n - 1:
            (l, r) = (1, 1)
            for j in range(len(sl)):
                if sl[j] < sl[j + 1]:
                    l += 1
                else:
                    break
            for j in range(len(sl)):
                if sl[-(j + 1)] < sl[-(j + 2)]:
                    r += 1
                else:
                    break
            if l > r:
                ans += 'L' * l
            else:
                ans += 'R' * r
            break
        elif current < sl[0] and sl[0] <= sl[-1]:
            ans += 'L'
            current = sl.pop(0)
        elif current < sl[-1] and sl[0] > sl[-1]:
            ans += 'R'
            current = sl.pop()
    elif current < sl[0] and current >= sl[-1]:
        ans += 'L'
        current = sl.pop(0)
    elif current >= sl[0] and current < sl[-1]:
        ans += 'R'
        current = sl.pop()
    else:
        break
print(len(ans))
print(ans)
