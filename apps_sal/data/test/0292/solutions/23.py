def n_of_nodes(h):
    result = 0
    for i in range(h):
        result += 2 ** i
    return result


h, n = tuple(map(int, input().split()))

way = ""
t = h
while t:
    if n % 2:
        way = "L" + way
        n //= 2
        n += 1
    else:
        way = "R" + way
        n //= 2
    t -= 1

answer = 1
current = "L"
t = h
for i in way:
    if i == current:
        answer += 1
        if current == "L":
            current = "R"
        else:
            current = "L"
    else:
        answer += n_of_nodes(t) + 1
    t -= 1

print(answer - 1)
