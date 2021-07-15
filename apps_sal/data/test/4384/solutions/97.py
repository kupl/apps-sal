N = input()
x = int(N)

if x > 0 and x < 1000:
    answer = 'ABC'
elif x >= 1000 and x <= 1998:
    answer = 'ABD'

print(answer)
