def scand():
    return int(input())
def scana():
    return [int(x) for x in input().split()]
n=scand()
a=scana()
summ=sum(a)
for i in range(max(a),10000):
    if(i*n-summ>summ):
        print(i)
        break

