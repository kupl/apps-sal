from collections import deque

def constructString( counts ):

    s = ""
    midLetter = ""
    for i , count in enumerate( counts ):
        if count > 0:
            letter = chr( ord('a') + i )
            if count % 2 == 1:
                midLetter = letter
            s += letter * ( count//2 )

    rs = s[::-1]

    return s + midLetter + rs

def __starting_point():

    counts = [0]*26

    s = input().strip()
    n = len(s)
    for c in s:
        counts[ord(c)-ord('a')] += 1

    maxOddNum = n%2
    curOddNum = 0
    needChangeLetters = deque()
    for i , count in enumerate(counts):
        if count%2 == 1:
            needChangeLetters.append( i )

    #print( needChangeLetters )
    while len(needChangeLetters) >= 2:
        preIndex = needChangeLetters.popleft()
        postIndex = needChangeLetters.pop()
        counts[preIndex] += 1
        counts[postIndex] -= 1

    print( constructString( counts ) )

__starting_point()
