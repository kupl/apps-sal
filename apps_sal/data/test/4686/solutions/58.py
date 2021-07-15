data = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
w = input()


for i in range(26):
        if w.count(data[i]) % 2 != 0:
            print('No')
            return
print('Yes')
