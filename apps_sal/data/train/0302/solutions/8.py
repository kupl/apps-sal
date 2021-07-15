class Solution:
     def validSquare(self, A, B, C, D):
         """
         A B   A D   A C
         C D   B C   D B
     
         A C   A B   A D     
         B D   D C   C B     
         
         - figure out which orientation this is
         - B-A == D-C and C-A == D-B
         - D-A == C-B and B-A == C-D 
         - C-A == B-D and D-A == B-C
         
         - if one of those is true, just need to check angles
         - check length of two perpendicular sides is same
             - enough to check -y, x?
             
         4     A(2,4)
         3
         2 C(0,2)  B(4,2)
         1
         0     D(2,0)
           0 1 2 3 4
           
         [1,0]
         [-1,0]
         [0,-1]
         [0,1]
         
         1       D
         
         0  B         A
         
        -1       C
         
           -1    0    1
         
         
         :type p1: List[int]
         :type p2: List[int]
         :type p3: List[int]
         :type p4: List[int]
         :rtype: bool
         """
         def sub(p2, p1):
             return [p2[0]-p1[0], p2[1]-p1[1]]
         
 #         def add(p1, p2):
 #             return [p1[0]+p2[0], p1[1]+p2[1]]
             
         if sub(A, B) == [0, 0]:
             return False
         
         if sub(B, A) == sub(D, C) and sub(C, A) == sub(D, B):
             print((1))
             diff1 = sub(B, A)
             diff2 = sub(A, C)
             print((diff1, diff2))
             if diff1 == [-diff2[1], diff2[0]] or diff1 == [diff2[1], -diff2[0]]:
                 return True
             
         elif sub(D, A) == sub(C, B) and sub(B, A) == sub(C, D):
             print((2))
             diff1 = sub(D, A)
             diff2 = sub(A, B)
             print((diff1, diff2))
             if diff1 == [-diff2[1], diff2[0]] or diff1 == [diff2[1], -diff2[0]]:
                 return True
             
             
         elif sub(C, A) == sub(B, D) and sub(D, A) == sub(B, C):
             print((3))
             diff1 = sub(C, A)
             diff2 = sub(A, D)
             print((diff1, diff2))  # [-1, -1] [1, -1]
             if diff1 == [-diff2[1], diff2[0]] or diff1 == [diff2[1], -diff2[0]]:
                 return True
             
         else:
             print((0))
             
         return False
             
         

