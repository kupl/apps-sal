from collections import deque

S = list(input())
Q = int(input())
answer = deque(S)
reverse = False
for _ in range(Q):
  query = input()
  if query == '1':
    reverse ^= True
  else:
    ope, types, alphabet = query.split()
    if types == '1':
      if reverse:
        answer.append(alphabet)
      else:
        answer.appendleft(alphabet)
    else:
      if reverse:
        answer.appendleft(alphabet)
      else:
        answer.append(alphabet)
if reverse:
  result = ''
  for i in range(len(answer)):
    result += answer.pop()
  print(result)
else:
  result = ''
  for i in range(len(answer)):
    result += answer.popleft()
  print(result)

