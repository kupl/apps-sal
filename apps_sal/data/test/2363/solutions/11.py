def larger(a,b,count):
    if b == 0:
        return count

    if a > b:
        a,b = b,a

    count += (b//a)
    count = larger(a,b%a,count)
    return count

testCase = input()
for _ in range(int(testCase)):
    a = list(map(int,input().split(' ')))
    print(larger(a[0],a[1],0))

