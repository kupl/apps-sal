s = input()
n = len(s)
smallest = ord(s[0])
print("Mike")
for i in range(1, n):
    if smallest < ord(s[i]):
        print("Ann")
    else:
        print("Mike")
        smallest = ord(s[i])
