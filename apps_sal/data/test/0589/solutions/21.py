input_str = input()
tmp = []
if input_str[0] == '?':
    result=9
    a = 11
    for c in input_str[1:]:
        if c == '?':
            result*=10
        elif 'A' <= c <= 'J' and tmp.count(c)==0:
            tmp.append(c)
            a-=1
            result*=a
elif 'A' <= input_str[0] <= 'J':
    tmp.append(input_str[0])
    result=9
    a=10
    for c in input_str[1:]:
        if c == '?':
            result*=10
        elif 'A' <= c <= 'J' and tmp.count(c)==0:
            tmp.append(c)
            a-=1
            result*=a
else:
    a=11
    result=1
    for c in input_str[1:]:
        if c == '?':
            result*=10
        elif 'A' <= c <= 'J' and tmp.count(c)==0:
            tmp.append(c)
            a-=1
            result*=a
print(result)
