ans = []
# code on gfg


def printMaxActivities(s, f):
    n = len(f)
    # The first activity is always selected
    i = 0
    ans.append(i)
    # Consider rest of the activities
    for j in range(n):
        # If this activity has start time greater than
        # or equal to the finish time of previously
        # selected activity, then select it
        if s[j] >= f[i]:
            ans.append(j)
            i = j

        # Driver program to test above function
n = int(input())
s = list(map(int, input().split()))
f = list(map(int, input().split()))
printMaxActivities(s, f)
print(*ans)
