def main():
  n=int(input())
  arr=input().split()
  for x in range(n):
    arr[x]=int(arr[x])
    arr.append(arr[x])
  count=0
  current=0
  current_count=0
  for x in range(len(arr)):
    if arr[x]==0 and current==1:
      count=max(count,current_count)
      current=0
      current_count=0
    elif arr[x]==1 and current==0:
      current=1
      current_count=1
    elif arr[x]==1 and current==1:
      current_count+=1
  print(count)
main()

