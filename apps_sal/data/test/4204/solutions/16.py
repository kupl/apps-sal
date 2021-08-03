txt = input()
n = int(input())
for i in range(n):
    if txt[i] != '1':
        print(txt[i])
        break
else:
    print("1")
