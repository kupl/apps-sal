n = input()
k = int(input())
for i in range(len(n)):
    if n[i] == '1':
        k -= 1
        if k == 0:
            print(1)
            break
    else:
        print(n[i])
        break
