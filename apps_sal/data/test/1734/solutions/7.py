def nash():
    n = int(input())
    numbers = [input() for i in range(n)]
    telep = {}
    count = 1
    for number in numbers:
        for l in range(1, len(number) + 1):
            for i in range(0, len(number) - l + 1):
                key = number[i: i + l]
                if key in telep and telep[key] != count:
                    telep[key] = -1
                else:
                    telep[key] = count
        count += 1
    reverse = {}
    for key in telep:
        if telep[key] == -1:
            continue
        elif telep[key] not in reverse:
            reverse[telep[key]] = key
        elif len(key) < len(reverse[telep[key]]):
            reverse[telep[key]] = key
    for i in range(1, n + 1):
        print(reverse[i])
nash()
        

