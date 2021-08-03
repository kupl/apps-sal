n = int(input())
s = input()

ans = "no"
for i in range(len(s)):
    if(s[i] == '.'):
        continue
    for d in range(1, 100):
        cnt = 1
        j = i + d
        while(cnt < 5):
            if(j >= len(s)):
                break
            if(s[j] == '.'):
                break
            cnt += 1
            j += d
        if(cnt == 5):
            ans = "yes"
            break
    if(ans == "yes"):
        break

print(ans)
