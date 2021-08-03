t = input().replace('5', '2').replace('9', '6')

s = input().replace('5', '2').replace('9', '6')


res = 10 ** 100


for i in t:

    res = min(res, s.count(i) // t.count(i))

print(res)


# Made By Mostafa_Khaled
