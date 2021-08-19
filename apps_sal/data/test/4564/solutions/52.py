from typing import List


S = list(input())  # type: List[str]
if len(S) == len(set(S)):
    print('yes')
else:
    print('no')
