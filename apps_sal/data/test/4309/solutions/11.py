a = int(input())
for i in range(10):
    if i * 111 >= a:
        print(i * 111)
        break
    else:
        continue
