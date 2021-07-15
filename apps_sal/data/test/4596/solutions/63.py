n = int(input())
ary = list(map(int, input().split()))

def count_ops(ary):
    count = 0

    while 1:
        for i, v in enumerate(ary):
            if v % 2 == 1:
                return count
            else:
                ary[i] = v/2

        count += 1
    
    return count
 
print((count_ops(ary)))

