word = ''
arr = [0]
for i in range(1,22000):
    word = word + str(i)
    arr.append(arr[-1] + len(word))
    
def sol(k):
    d = 0
    for i in range(1,22000):
        if arr[i] > k:
            d = i - 1
            break
    
    k = k - arr[d]
    if k == 0:
        return str(d)[-1]
    else:
        return word[k - 1]
    
for i in range(int(input())):
    print(sol(int(input())))
