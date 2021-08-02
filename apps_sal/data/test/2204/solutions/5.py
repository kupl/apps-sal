import sys


def input():
    return sys.stdin.readline().rstrip()


def input_split():
    return [int(i) for i in input().split()]


testCases = int(input())
answers = []
for test in range(testCases):
    # take input
    n, m = input_split()
    arr = []
    barr = []
    for _ in range(m):
        a, b = input_split()
        arr.append(a)
        barr.append(b)

    temp1 = [(arr[i], 1, i) for i in range(m)]
    temp2 = [(barr[i], 2, i) for i in range(m)]

    mixed = temp1 + temp2
    mixed.sort()
    mixed.reverse()

    pointer = 0
    done = 0
    maxi = 0
    score = 0
    unlocked = [False for i in range(m)]
    while(done < n and pointer < 2 * m):
        val, typ, index = mixed[pointer]
        if typ == 1:
            done += 1
            score += val
            unlocked[index] = True
            if done == n:
                maxi = max(score, maxi)
        else:
            if not unlocked[index]:
                potential = score + (n - done - 1) * val + arr[index]
            else:
                potential = score + (n - done) * val
                # can break here?
            maxi = max(potential, maxi)

        pointer += 1

    ans = maxi
    answers.append(ans)

    if test != testCases - 1:
        blank = input()

print(*answers, sep='\n')
