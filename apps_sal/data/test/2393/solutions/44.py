t = int(input())
strings = [input() for _ in range(t)]
for string in strings:
    n = len(string)
    ans = string.count('one') + string.count('two') - string.count('twone')
    print(ans)
    i = 0
    f = True
    answers = []
    while i < n - 2:
        if string[i:i + 3] == "one":
            answers.append(i + 2)
            i += 3
            continue
        else:
            if i < n - 4 and string[i:i + 5] == "twone":
                answers.append(i + 3)
                i += 5
                continue
            else:
                if string[i:i + 3] == "two":
                    answers.append(i + 2)
                    i += 3
                    continue
        i += 1
    print(*answers)

