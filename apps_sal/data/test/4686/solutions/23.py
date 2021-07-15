w = input()
for i in range(len(w)):
    if w.count(w[i]) % 2 == 1:
        print('No')
        return
print('Yes')
