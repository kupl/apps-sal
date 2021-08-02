n = int(input())
my_str = input().upper()
alphabet = "QWERTYUIOPASDFGHJKLZXCVBNM"
i = 0
while i < 26 and alphabet[i] in my_str:
    i += 1
if i == 26:
    print("YES")
else:
    print("NO")
