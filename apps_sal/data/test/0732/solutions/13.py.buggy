num = int(input())
cou = 0


def traverse(x):
    if(x > num):
        return
    nonlocal cou
    if(len(set([int(j) for j in str(x)])) <= 2):
        cou += 1
        for i in range(0, 10):
            traverse(10 * x + i)


for i in range(1, 10):
    traverse(i)
print(cou)
