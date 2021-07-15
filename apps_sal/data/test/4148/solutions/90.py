N = int(input())
S = input()
ans = ""

for i in range(len(S)):
    ans += chr(int(ord("A"))+(int(ord(S[i])+N)-int(ord("A")))%26)

print(ans)
