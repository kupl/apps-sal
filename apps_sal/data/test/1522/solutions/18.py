n = int(input())
string = input()
ans = 0
current = [0 for i in range(26)]
for i in range(0, len(string)):
    if i % 2 == 0:
        current[ord(string[i]) - 97] += 1
    elif current[ord(string[i]) + 32 - 97] != 0:
        current[ord(string[i]) + 32 - 97] -= 1
    else:
        ans += 1
print(ans)
