n,m=map(int,input().split())
print(*['#'*(m+2)]+['#'+input()+'#' for _ in range(n)]+['#'*(m+2)],sep='\n')
