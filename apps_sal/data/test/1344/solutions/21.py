n = input()
str_arr = input().split(' ')
arr = [int(num) for num in str_arr]
lm = 1
l = 1
ant = arr[0]
for act in arr:
    if act > ant:
        l += 1
        if l > lm:
            lm = l
    else:
        l = 1
    ant = act

print(lm)
