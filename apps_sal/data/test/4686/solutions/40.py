li = [0]*26
w = input()
for i in range(len(w)):
    li[ord(w[i])-97] += 1
for i in range(26):
    if li[i] % 2 == 1:
        print("No")
        return
print("Yes")
