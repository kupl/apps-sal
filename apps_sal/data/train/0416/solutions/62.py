from collections import deque
class Solution:
    def catMouseGame(self, graph):
      
        arr = [[[0]*2 for j in range(55)] for i in range(55)]
        q=deque()
        for i in range(1,len(graph)):
            arr[i][i][0],arr[i][i][1]=2,2
            arr[i][0][0],arr[i][0][1]=1,1
            q.append((i,0,0))
            q.append((i,0,1))
            q.append((i,i,0))
            q.append((i,i,1))
        while q:
            c,m,turn = q.popleft()
            s = arr[c][m][turn]
            if turn==0:
                
                for pre_move in graph[m]:
                    if arr[c][pre_move][1]!=0:
                        continue
                    if s==1:
                        arr[c][pre_move][1]=1
                        q.append((c,pre_move,1))
                    elif s==2:
                        cat_win=True
                        for nex_move in graph[pre_move]:
                            if arr[c][nex_move][0]!=2:
                                cat_win=False
                                break
                        if cat_win:
                            arr[c][pre_move][1]=2
                            q.append((c,pre_move,1))
            else:
                for pre_move in graph[c]:
                    if arr[pre_move][m][0]!=0:
                        continue
                    if pre_move!=0:
                        if s==2:
                            arr[pre_move][m][0]=2
                            q.append((pre_move,m,0))
                        elif s==1:
                            mouse_win=True
                            for nex_move in graph[pre_move]:
                                if nex_move!=0:
                                    if arr[nex_move][m][1]!=1:
                                        mouse_win=False
                                        break
                            if mouse_win:
                                arr[pre_move][m][0]=1
                                q.append((pre_move,m,0))
        return arr[2][1][1]
