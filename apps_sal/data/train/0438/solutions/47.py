class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        lengthStartingWith = {}
        lengthEndingWith = {}
        relevantStartingIndices = {}
        
        bestIndex = -1
        for index,j in enumerate(arr):
            print(index)
            i = j-1
            leftNeighbor = i-1
            rightNeighbor = i+1
            if(leftNeighbor in lengthEndingWith and rightNeighbor in lengthStartingWith):
                leftLength = lengthEndingWith[leftNeighbor]
                rightLength = lengthStartingWith[rightNeighbor]
                lengthEndingWith.pop(leftNeighbor)
                lengthStartingWith.pop(rightNeighbor)
                if(rightNeighbor in relevantStartingIndices):
                    relevantStartingIndices.pop(rightNeighbor)
                lengthStartingWith[leftNeighbor-leftLength+1] = leftLength + rightLength + 1
                if(leftLength + rightLength + 1 == m):
                    relevantStartingIndices[leftNeighbor-leftLength+1] = True
                else:
                    if(leftNeighbor-leftLength+1 in relevantStartingIndices):
                        relevantStartingIndices.pop(leftNeighbor-leftLength+1)
                lengthEndingWith[rightNeighbor+rightLength-1] = leftLength + rightLength + 1
                
            
            elif(leftNeighbor in lengthEndingWith):
                leftLength = lengthEndingWith[leftNeighbor]
                lengthEndingWith.pop(leftNeighbor)
                lengthStartingWith[leftNeighbor-leftLength+1] = leftLength + 1
                lengthEndingWith[i] = leftLength + 1
                
                if(leftLength + 1 == m):
                    relevantStartingIndices[leftNeighbor-leftLength+1] = True
                else:
                    if(leftNeighbor-leftLength+1 in relevantStartingIndices):
                        relevantStartingIndices.pop(leftNeighbor-leftLength+1)
                
            elif(rightNeighbor in lengthStartingWith):
                rightLength = lengthStartingWith[rightNeighbor]
                lengthStartingWith.pop(rightNeighbor)
                lengthEndingWith[rightNeighbor+rightLength-1] = rightLength + 1
                lengthStartingWith[i] = rightLength + 1
                
                if(rightNeighbor in relevantStartingIndices):
                    relevantStartingIndices.pop(rightNeighbor)
                if(rightLength + 1 == m):
                    relevantStartingIndices[i] = True
                else:
                    if(i in relevantStartingIndices):
                        relevantStartingIndices.pop(i)
                
            
            else:
                #print(\"here4\")
                #print(i)
                lengthEndingWith[i] = 1
                lengthStartingWith[i] = 1
                
                if(m == 1):
                    relevantStartingIndices[i] = True
                else:
                    if(i in relevantStartingIndices):
                        relevantStartingIndices.pop(i)
            
            if(len(relevantStartingIndices) > 0):
                bestIndex = index + 1
        return bestIndex
            

