num_a = ord("A")
num_z = ord("Z")

N = int(input())
S = input()
ans = ""
for char in S:
    tmp = N + ord(char)
    if tmp > num_z:
        ans += chr(tmp - 26)
    else:
        ans += chr(tmp)
print(ans)
