from fractions import Fraction
S = int(input())

l = S // 3
#r = S%3

#print ('l=' + str(l))
c = 1
count = 1

if S < 3:
    count = 0

for i in range(1, l):
    #c *=  (S-3*i-3)*(S-3*i-4)*(S-3*i-5)/((S-2*i-3)*(S-2*i-4))/(i+1)
    c = Fraction(c * (S - 3 * i) * (S - 3 * i - 1) * (S - 3 * i - 2), ((S - 2 * i - 1) * (S - 2 * i - 2)) * i)

    #cp =  (S-3*i)*(S-3*i-1)*(S-3*i-2)
    # ci=(S-2*i-1)*(S-2*i-2)
    #c = c * cp / ci / i
    # print('c'+str(i)+'='+str(c))

    count += c
    # print('count'+str(i)+'='+str(count))
    #count = int(count)%(10**9+7)


# print('cp='+str(cp))
# print('ci='+str(ci))
# print('c='+str(c))
# print('count='+str(count))


answer = int(count) % (10**9 + 7)
print(answer)
