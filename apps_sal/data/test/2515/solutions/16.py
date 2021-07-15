def isPrime(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False

    for i in range(3, int(num**0.5)+1, 2):
        if num % i == 0:
            return False
    return True

def is_2017(num):
    temp = (num + 1) // 2
    if isPrime(num) and isPrime(temp):
        return True
    else:
        return False

def __starting_point():
    
    is_2017_list = [0] * (10**5 + 1)
    count = 0
    for i in range(1, 10**5):
        if is_2017(i):
            count += 1
            is_2017_list[i] = count
            
        else:
            is_2017_list[i] = count

    Q = int(input())

    ans_list = []
    for _ in range(Q):
        l, r = list(map(int, input().split()))
        ans = is_2017_list[r] - is_2017_list[l-1]
        ans_list.append(ans)
    
    for ans in ans_list:
        print(ans)

    



__starting_point()
