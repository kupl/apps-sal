N = int(input())
A = sorted(list(map(int, input().split())), reverse=True)


def sameA(List):
    for i in range(len(List)):
        try:
            if List[i] == List[i + 1]:
                ans = List[i]
                anslist = A[i + 2:]
                return (ans, anslist)
        except IndexError:
            return (False, False)


(a1, list1) = sameA(A)
if not a1 == False:
    (a2, list2) = sameA(list1)
    if not a2 == False:
        print(a1 * a2)
    else:
        print(0)
else:
    print(0)
