H, W=map(int, input().split())
out=['#'*(W+2)]+['#'+input()+'#' for _ in range(H)]+['#'*(W+2)]
print(*out, sep='\n')

